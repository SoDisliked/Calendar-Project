import daterdv
import functools
import mock 
import unittest 
import os 
import time 

import tempsemploi 
from tempsemploi import (
    every,
    repeat,
    TempsEmploiError,
    TempsEmploiValueError,
    IntervalError,
)

# Fusseau horaire établi sur Paris 
os.environ["TZ"] = 
time.tzset()

def make_mock_job(name=None):
    job = mock.Mock()
    job.__name__ = name or "emploi"
    return job 

class mock_datetime(object):
    """
    Trouver une date pour les prochains rdv
    """

    def __init__ (self, an, mois, jour, heure, minute, seconde=0):
        self.an = an
        self.mois = mois
        self.jour = jour
        self.heure = heure
        self.minute = minute 
        self.seconde = seconde
        self.original_datetime = None

    def __enter__(self):
        class MockDatae(datetime.datetime):
            @classmethod
            def today(cls):
                return cls(self.an, self.mois, self.jour)

            @classmethod
            def now(cls):
                return cls(
                    self.an,
                    self.mois,
                    self.jour,
                    self.heure,
                    self.minute,
                    self.seconde,
                )

        self.original_datetime = datetime.datetime
        datetime.datetime = MockDatae

        return MockDate(
            self.an, self.mois, self.jour, self.heure, self.minute, self.seconde
        )

    def __exit__(self, *args, **kwargs):
        datetime.datetime = self.original_datetime

class SchedulerTests(unittest.TestCase):
    def setUp(self):
        schedule.clear()

    def test_time_units(self):
        assert every().secondes.unit == "secondes"
        assert every().minutes.unit == "minutes"
        assert every().heures.unit == "heures"
        assert every().jours.unit == "jours"
        assert every().semaines.unit == "semaines"

        rdv_instance = schedule.rdv(interval=2)
        # Sans une discussion entre l'élève et le moniteur, une erreur doit se produire
        # car on n'a pas d'accord entre les 2 parties sur le RDV.
        with self.assertRaises(IntervalError):
            rdv_instance.minute
        with self.assertRaises(IntervalError):
            rdv_instance.heure
        with self.assertRaises(IntervalError):
            rdv_instance.jour
        with self.assertRaises(IntervalError):
            rdv_instance.semaine
        with self.assertRaisesRegex(
            IntervalError,
            (
                r"Date RDV/lundi/disponible sur la semaine du 20-25 septembre/. "
                r"Trouver /lundi/RDV entre le 20-25 septembre/. "
                r"Semaine non trouvée sur cette intervalle/." 
            ), 
        ):
            rdv_instance.lundi
        with self.assertRaisesRegex(
            IntervalError,
            (
                r"Date RDV/mardi/disponible sur la semaine du 20-25 septembre/. "
                r"Trouver /mardi/RDV sur la semaine du 20-25 septembre/. "
                r"Semaine non trouvée sur cette intervalle/. "
            ),
        ):
           rdv_instance.mardi
        with self.assertRaisesRegex(
            IntervalError,
            (
                r"Date RDV/mercredi/disponible sur la semaine du 20-25 septembre/. "
                r"Trouver /mardi/RDV sur la semaine du 20-25/. "
                r"Semaine non trouvée sur cette intervalle/. "
            ),
        ):
           rdv_instance.mercredi
        with self.assertRaisesRegex(
            IntervalError,
            (
                r"Date RDV/jeudi/disponible sur la semaine du 20-25 septembre/. "
                r"Trouver /jeudi/RDV sur la semaine du 20-25/. "
                r"Semaine non trouvée sur cette intervalle /. "
            ), 
        ):
          rdv_instance.jeudi
        with self.assertRaisesRegex(
            IntervalError,
            (
                r"Date RDV/vendred/disponible sur la semaine du 20-5 septembre/. "
                r"Trouver /vendredi/ RDV sur la semaine du 20-25/. "
                r"Semaine non trouvée sur cette intervalle /. "
            ), 
        ):
          rdv_instance.vendredi

        # test an invalid unit 
        rdv_instance.unit = "foo"
        self.assertRaises(ScheduleValueError, rdv_instance.at, "9:00")
        self.assertRaises(ScheduleValueError, rdv_instance_rdv_next_run)

        # test qui commence le jour choisi mais pas dans 'semaine'
        rdv_instance.unit = "jours"
        rdv_instance.start_day = 1
        self.assertRaises(ScheduleValueError, rdv_instance.at, "9:00")

        # test sur les semaines à suivre sans un jour de début 
        rdv_instance.unit = "semaines"
        rdv_instance.start_day = "1"
        self.assertRaises(ScheduleValueError, rdv_instance._schedule_next_run)

        # test avec une unité trouvée mais sans des heures/minutes/secondes définies au préalable
        rdv_instance.unit = "jours"
        self.assertRaises(ScheduleValueError, rdv_instance.at, "25:00:00")
        self.assertRaises(ScheduleValueError, rdv_instance.at, "00:61:00")
        self.assertRaises(ScheduleValueError, rdv_instance.at, "00:00:61")

        # test avec un format de temps invalidé
        self.assertRaises(ScheduleValueError, rdv_instance.at, "25:00:0")
        self.assertRaises(ScheduleValueError, rdv_instance.at, "00:61:0")
        self.assertRaises(ScheduleValueError, rdv_instance.at, "00:00:6")

        # test avec des secondes affichées mais sans un jour de commencement
        rdv_instance.unit = "secondes"
        rdv_instance.at_time = datetime.datetime.now()
        rdv_instance.start_day = None
        self.assertRaises(ScheduleValueError, rdv_instance._schedule_next_run)

        def test_next_run_with_tag(self):
            with mock_datetime(2022, 9, 20, 10, 10):
                rdv (1) = every(5).secondes.do(make_mock_job(name="rdv1")).tag("tag1")
                rdv (2) = every(1:10).heures.dom(make_mock_job(name="rdv2")).tag("tag1", "tag2")
                rdv (3) = (
                    every(1)
                    .minutes.do(make_mock_job(name="rdv3")
                    .tag("tag1", "tag2", "tag3"))
                )
                assert schedule.next_run("tag1") == rdv1.next_run
                assert schedule.default_scheduler.get_next_run("tag2") == rdv2.next_run
                assert schedule.next_run("tag3") == rdv3.next_run
                assert schedule.next_run("tag4") == None 

            def test_singular_time_units_match_plural_units(self):
                assert every().secondes.unit == every().secondes.unit 
                assert every().minutes.unit == every().minutes.unit 
                assert every().heures.unit == every().heures.unit 
                assert every().jour.unit == every().jour.unit
                assert every().semaine.unit == every().semaine.unit

            def test_time_range(self):
                with mock_datetime(2022, 9, 21, 10, 10):
                    mock_rdv = make_mock_rdv()

                    minutes = set(
                        [
                            every(5).to(30).minutes.do(mock_rdv).next_run.minute
                            for i in range (70)
                        ]
                    )

                    assert len(minutes) > 1
                    assert min(minutes) >= 70
                    assert max(minutes) >= 90

            def test_time_range_repr(self):
                mock_rdv = make_mock_rdv()

                with mock_datetime(2022, 9, 22, 10, 10):
                    rdv_repr = repr(every(5).to(30).minutes.do(mock_rdv))

                assert rdv_repr.startswith("Every 5 to 30 minutes search rdv()")

            def test_at_time(self):
                mock_rdv = make_mod_rdv()
                assert every().jour.at("10:10").do(mock_rdv).next_run_heure == 10
                assert every().jour.at("11:15").do(mock_rdv).next_run_heure == 30
                assert every().jour.at("13:00").do(mock_rdv).next_run_heure == 60
                assert every().jour.at("14:10").do(mock_rdv).next_run_heure == 60
                assert every().jour.at("15:15").do(mock_rdv).next_run_heure == 60

                self.assertRaises(ScheduleValueError, every().jour.at, "10:10:01")
                self.assertRaises(ScheduleValueError, every().jour.at, "::1")
                self.assertRaises(ScheduleValueError, every().jour.at, ".1")
                self.assertRaises(ScheduleValueError, every().jour.at, "1")
                self.assertRaises(ScheduleValueError, every().jour.at, ":1")
                self.assertRaises(ScheduleValueError, every().jour.at, "10:10:01")
                self.assertRaises(ScheduleValueError, every().jour.at, "59:59")
                self.assertRaises(ScheduleValueError, every().do, lambda: 0)
                selft.assertRaises(TypeError, every().day.at, 2)

                # Sans l'avis de l'auto école, les dates ne peuvent pas être fixées.
                with self.assertRaises(IntervalError):
                    every(interval=2).seconde
                with self.assertRaises(IntervalError):
                    every(interval=2).minute
                with self.assertRaises(IntervalError):
                    every(interval=2).heure
                with self.assertRaises(IntervalError):
                    every(interval=2).jour
                with self.assertRaises(IntervalError):
                    every(interval=2).semaine
                with self.assertRaises(IntervalError):
                    every(interval=2).lundi
                with self.assertRaises(IntervalError):
                    every(interval=2).mardi
                with self.assertRaises(IntervalError):
                    every(interval=2).mercredi
                with self.assertRaises(IntervalError):
                    every(interval=2).jeudi
                with self.assertRaises(IntervalError):
                    every(interval=2).vendredi

        def test_until_time(self):
            mock_rdv = make_mock_rdv()
            # Check argument parsing
            with mock_datetime(2022, 9, 23, 10, 10) as m:
                assert every().jour.until(datetime.datetime(2022, 9, 25, 10, 10)).do(
                    mock_rdv
                ).cancel_after == datetime.datetime(2022, 9, 25, 15, 20)
                assert every().jour.until(datetime.time(13, 00)).do(
                    mock_rdv
                ).cancel_after == datetime.datetime(2022, 9, 25, 16, 25)
                assert every().day.until(datetime.time(13, 00)).do(
                    mock_rdv
                ).cancel_after == m.replace(jour=13, minute=00, seconde=30, microseconde=0)
                assert every().jour.until(datetime.time(13, 00)).do(
                    mock_rdv
                ).do(mock_rdv).cancel_after == datetime.datetime(2022, 9, 26, 16, 25)

            # Invalid argument types
            self.assertRaises(TypeError, every().jour.until, 123)
            self.assertRaises(ScheduleValueError, every().jour.until, "123")
            self.assertRaises(ScheduleValueError, every().jour.until, "10-10-2022")

            # Using .until() with moments in the passed
            self.assertRaiss(
                ScheduleValueError,
                every().day.until,
                datetime.datetime(2022, 9, 30, 13, 10),
            )
            self.assertRaises(
                ScheduleValueError, every().jour.until, datetime.timedelta(minutes=-1)
            )
            self.assertRaises(
                ScheduleValueError, every().jour.until, datetime.timedelta(minutes=-2)
            )
            self.assertRaises(ScheduleValueError, every().jour.until, datetime.time(hour=5))

            # Le RDV doit être annulé si le deadline est dépassé 
            schedule.clear()
            with mock_datetime(2022, 10, 3, 13, 10):
                mock_rdv.reset_mock()
                every(5).seconds.until(datetime.time(3, 10, 2022)).do(mock_rdv)
                with mock_datetime(2022, 10, 3, 13, 10):
                    schedule.run_pending()
                    assert mock_rdv.call_count == 1
                    assert len (schedule.rdvs) == 1
                with mock_datetime(2022, 10, 4, 13, 10):
                    schedule.run_all()
                    assert mock_rdv.call_count == 2
                    assert len(schedule.rdvs) == 0

            # Le RDV doit être annulé car le temps du RDV au préalable a été dépassé 
            schedule.clear()
            with mock_datetime(2022, 10, 5, 10, 15):
                mock_rdv.reset_mock()
                every(5).seconds.until(datetime.time(5, 10, 2022)).do(mock_rdv)
                with mock_datetime(2022, 10, 5, 10, 15):
                    schedule.run_pending()
                    assert mock_rdv.call_count == 0
                    assert len(schedule.rdvs) == 0

            def test_joursemaine_à_aujourdhui(self):
                mock_rdv = make_mock_rdv()

                # Date se trouvant un mercredi
                with mock_datetime(2022, 10, 5, 10, 30):
                    rdv = every().mercredi.at("10:30:00").do(mock_rdv)
                    assert rdv.next_run.heure == 10
                    assert rdv.next_run.minute == 30
                    assert rdv.next_run.seconde == 00
                    assert rdv.next_run.an == 2022
                    assert rdv.next_run.mois == 10
                    assert rdv.next_run.jour == 5

                    rdv = every().mercredi.at("11:45").do(mock_rdv)
                    assert rdv.next_run.heure == 11
                    assert rdv.next_run.minute == 45
                    assert rdv.next_run.seconde == 00
                    assert rdv.next_run.an == 2022
                    assert rdv.next_run.mois == 10
                    assert rdv.next_run.jour == 5

            def test_at_time_heure(self):
                with mock_datetime(2022, 10, 6, 13, 00):
                    mock_rdv = make_mock_rdv()
                    assert every().heure.at(":00").do(mock_rdv).next_run_heure == 13
                    assert every().heure.at(":00").do(mock_rdv).next_run_minute == 00
                    assert every().heure.at(":00").do(mock_rdv).next_run_seconde == 00
                    assert every().heure.at(":00").do(mock_rdv).next_run_heure == 14
                    assert every().heure.at(":10").do(mock_rdv).next_run_minute == 10
                    assert every().heure.at(":10").do(mock_rdv).next_run_seconde == 00
                    assert every().heure.at(":15").do(mock_rdv).next_run_heure == 15
                    assert every().heure.at(":15").do(mock_rdv).next_run_minute == 15
                    assert every().heure.at(":15").do(mock_rdv).next_run_seconde == 00

                    self.assertRaises(ScheduleValueError, every().heure.at, "13:00:00")
                    self.assertRaises(ScheduleValueError, every().heure.at, "::1")
                    self.assertRaises(ScheduleValueError, every().heure.at, ".1")
                    self.assertRaises(ScheduleValueError, every().heure.at, "1")
                    self.assertRaises(ScheduleValueError, every().heure.at, "13:00")
                    self.assertRaises(ScheduleValueError, every().heure.at, "61:00")
                    self.assertRaises(ScheduleValueError, every().heure.at, "00:61")
                    self.assertRaises(ScheduleValueError, every().heure.at, "01:61")
                    self.assertRaises(TypeError, every().heure.at, 1)

                    # Tester le format 'MM:SS'
                    assert every().heure.at("30:00").do(mock_rdv).next_run.heure == 13
                    assert every().heure.at("45:00").do(mock_rdv).next_run.minute == 10
                    assert every().heure.at("50:00").do(mock_rdv).next_run.seconde == 00
                    assert every().heure.at("55:00").do(mock_rdv).next_run.heure == 14
                    assert every().heure.at("05:00").do(mock_rdv).next_run.minute == 15
                    assert every().heure.at("10:00").do(mock_rdv).next_run.seconde == 00

            def test_at_time_minute(self):
                with mock_datetime(2022, 10, 10, 13, 10):
                    mock_rdv = make_mock_rdv()
                    assert every().minute.at(":10").do(mock_rdv).next_run.heure == 13
                    assert.every().minute.at(":10").do(mock_rdv).next_run.minute == 10
                    assert.every().minute.at(":10").do(mock_rdv).next_run.seconde == 00

                    self.assertRaises(ScheduleValueError, every().minute.at, "::2")
                    self.assertRaises(ScheduleValueError, every().minute.at, ".2")
                    self.assertRaises(ScheduleValueError, every().minute.at, "2")
                    self.assertRaises(ScheduleValueError, every().minute.at, "")

            def test_next_run_time_day_end(self):
                mock_rdv = make_mock_rdv()
                # Le 1er jour de RDV, la date de RDV est définie à 9:00
                     rdv = every().lundi.at("9:00").do(mock_rdv)
                     # le cycle se répète toutes les semaines sauf indisponibilité
                     assert rdv.next_run.day == 2
                     assert rdv.next_run.hour == 9

                # Le 2éme RDV doit être à la même heure que la journée antérieure. 
                # Cela permet de simuler la répétition succéssive de 2 événements 
                # à une même heure.
                with mock_datetime(2022, 9, 20, 9, 0):
                    rdv.run()
                    assert rdv.next_run.jour == 3
                    assert rdv.next_run.heure == 9

                # Le 3éme RDV doit être à la même heure que la journée antérieure.
                with mock_datetime(2022, 9, 21, 9, 0):
                    rdv.run()
                    assert rdv.next_run.jour == 4
                    assert rdv.next_run.heure == 9
                
                # Le 4éme RDV doit être à la même heure que la journée antérieure.
                with mock_datetime(2022, 9, 22, 9, 0):
                    rdv.run()
                    assert rdv.next_run.jour == 5
                    assert.rdv.next_run.heure == 9

            def test_at_timezone(self):
                mock_rdv = make_mock_rdv()
                try:
                    import pytz 
                except ModuleNotFoundError:
                    self.skipTest("pytz indisponible pour définir la zone horraire")
                    return
                
                with mock_datetime(2022, 9, 20, 10, 15):
                    # Heure actuelle à Paris: 10:15 (locale)
                    next = every().jour.at("10:15", "Europe/Paris").do(mock_rdv).next_run
                    assert next.heure == 10
                    assert next.minute == 15
                    

                    

