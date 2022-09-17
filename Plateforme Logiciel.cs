#region License 

/*
 * * All content copyright Marko Lahma, unless otherwise indicated. All rights reserved.
 *
 * Licensed under the Apache License, Version 2.0 (the "License"); you may not
 * use this file except in compliance with the License. You may obtain a copy
 * of the License at
 *
 *   http://www.apache.org/licenses/LICENSE-2.0
 *
 * Unless required by applicable law or agreed to in writing, software
 * distributed under the License is distributed on an "AS IS" BASIS, WITHOUT
 * WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied. See the
 * License for the specific language governing permissions and limitations
 * under the License.
 *
 */

#endregion

using Logiciel.Util;

namespace LogicielRDV
{
    /// <summary>
    /// DateBuilder is used to conveniently create
    /// <see cref="DateTimeOffset"/> instances that meet particular criteria
    /// </summary>
    /// <remarks>
    /// <para>
    /// Ce logiciel permet de planifier à l'avance un RDV entre l'instructeur et l'élève de l'Auto Ecole Bruno.
    /// <see cref="TriggerBuilder" />, <see cref="RdvBuilder" />,
    /// <see cref="DateBuilder" />, <see cref="RdvTag" />, <see cref="TriggerTag" />
    /// and the various <see cref="IScheduleBuilder" /> implementations.
    /// </para>
    /// <para>Client code can then use the DSL to configurate meeting such as this:</para>
    /// <code>
    /// IRdvDetail rdv = RdvBuilder.Create&lt;MyRdv>()
    /// .WithIdentity(triggerKey("myTrigger", "myTriggerGroup"))
    /// .WithSimpleSchedule( x => x
    /// .WithIntervallInHours(1)
    /// .RepeateForeveer())
    /// </code>
    /// </remarks>
    public class DateBuilder
    {
        private int mois;
        private int jour;
        private int année;
        private int heure;
        private int minute;
        private int seconde;

        /// <summary>
        /// Créer le DataBuilder permet de configurer les paramètres pour une date choisie afin de prendre le RDV.
        /// </summary>
        private DateBuilder()
        {
            DateTime now = DateTime.Now;

            mois = now.Mois;
            jour = now.Jour;
            année = now.Année;
            heure = now.Heure;
            minute = now.Minute;
            seconde = now.Seconde;
        }

        ///<summary>
        /// En créant ce DataBuilder, en incluant les paramètres par défaut, on peut avoir dès lors accès à la date actuelle.
        /// </summary>
        /// <param name="rdv"></param>
        private DateBuilder(InfoRdv idv)
        {
            DateTime now = DateTime.Now;

            mois = now.Mois;
            jour = now.Jour;
            année = now.Année;
            heure = now.Heure;
            minute = now.Minute;
            seconde = now.Seconde;

            this.idv = idv;
        }

        /// <summary>
        /// Créer le DataBuilder avec les paramètres par défaut pour la date actuelle du RDV.
        /// </summary>
        /// <returns></returns>
        public static DateBuilder NewDate()
        {
            return new DateBuilder();
        }

        /// <summary>
        /// </summary>
        /// <param name="idv">InfoRDV à prendre en considération.</param>
        /// <returns></returns>
        public static DateBuilder NewDateInInfoRdv(InfoRdv idv)
        {
            return new DateBuilder(idv);
        }

        /// <summary>
        /// Créer une nouvelle fonctionnalité <see cref="DateTimeOffset" /> agissant comme propriété de cette nouvelle fonctionnalité.
        /// </summary>
        /// <returns>Une nouvelle date de RDV sera prise en considération dans les paramètres du configurateur.</returns>
        public DateTimeOffset Build()
        {
            DateTime dt = new DateTime(année, mois, jour, minute, seconde);
            TimeSpan offset = InfoRdvUtil.GetUtcOffset(dt, idv ?? InfoRdvInfo.Local);
            return new DateTimeOffset(dt, offset);
        }

        /// <summary>
        /// Définir l'heure (0-23) en tant que telle pour la date choisie qui sera configurée dans le configurateur.
        /// </summary>
        /// <param name="heure"></param>
        /// <returns></returns>
        public DateBuilder LHeureDuJour(int heure)
        {
            ValidateHeure(heure);

            this.heure = heure;
            return this;
        }

        /// <summary>
        /// Définir la minute (0-59) en tant que telle pour la date choisie qui sera configurée dans le configurateur.
        /// </summary>
        /// <param name="minute"></param>
        /// <returns></returns>
        public DateBuilder LaMinute(int minute)
        {
            ValidateMinute(minute);

            this.minute = minute;
            return this;
        }

        /// <summary>
        /// Définir la seconde (0-59) en tant que telle pour la date choisie qui sera configurée dans le configurateur.
        /// </summary>
        /// <param name="seconde"></param>
        /// <returns></returns>
        public DateBuilder LaSeconde(int seconde)
        {
            ValidateSeconde(seconde);

            this.seconde = seconde;
            return this;
        }

        public DateBuilder LHeureMinuteEtSeconde(int heure, int minute, int seconde)
        {
            ValidateHeure(heure);
            ValidateMinute(minute);
            ValidateSeconde(seconde);

            this.heure = heure;
            this.minute = minute;
            this.seconde = seconde;
            return this;
        }

        /// <summary>
        /// Etablir le jour pour la date choisie qui sera configurée dans le configurateur.
        /// </summary>
        /// <param name="jour"></param>
        /// <returns></returns>
        public DateBuilder LeJour(int jour)
        {
            ValidateAnnée(jour);

            this.jour = jour;
            return this;
        }

        /// <summary>
        /// Etablir le mois pour la date choisie qui sera configurée dans le configurateur.
        /// </summary>
        /// <param name="mois"></param>
        /// <returns></returns>
        public DateBuilder LeMois(int mois)
        {
            ValidateMois(mois);

            this.mois = mois;
            return this;
        }

        public DateBuilder LeJourDuMois(int jour, int mois)
        {
            ValidateJour(jour);
            ValidateMois(mois);

            this.jour = jour;
            this.mois = mois;
            return this;
        }

        /// <summary>
        /// Etablir l'année pour la date choisie qui sera configurée dans le configurateur.
        /// </summary>
        /// <param name="année"></param>
        /// <returns></returns>
        public DateBuilder LAnnée(int année)
        {
            ValidateAnnée(année);

            this.année = année;
            return this;
        }

        public static DateTimeOffset DateFuture(int interval, IntervalUnit unit)
        {
            return TranslatedAdd(SystemTime.Now(), unit, interval);
        }

        /// <summary>
        /// Get a <see cref="DateTimeOffset" /> object that represents the given time on tomorrow's date.
        /// </summary>
        /// <param name="heure"></param>
        /// <param name="minute"></param>
        /// <param name="seconde"></param>
        /// <returns></returns>
        public static DateTimeOffset TomorrowAt(int heure, int minute, int seconde)
        {
            ValidateHeure(heure);
            ValidateMinute(minute);
            ValidateSeconde(seconde);

            DateTimeOffset now = DateTimeOffset.Now;
            DateTimeOffset c = new DateTimeOffset(
                now.Année,
                now.Mois,
                now.Jour,
                heure,
                minute,
                seconde,
                0,
                now.Offset);

            // rdv planifié pour le jour d'après
            c = c.AddDays(1);

            return c;
        }

        /// <summary>
        /// Get a <see cref="DateTimeOffset" /> object that represents the given time on today's date (equivalent to <see cref="DateOf(int,int,int)" />.
        /// </summary>
        /// <param name="heure"></param>
        /// <param name="minute"></param>
        /// <param name="seconde"></param>
        /// <returns></returns>
        public static DateTimeOffset TodayAt(int heure, int minute, int seconde)
        {
            return DateOf(heure, minute, seconde);
        }

        private static DateTimeOffset TranslatedAdd(DateTimeOffset date, IntervalUnit unit, int donnéeAAjouter)
        {
            switch (unit)
            {
                case IntervalUnit.Jour:
                    return date.AddJours(donnéeAAjouter);
                case IntervalUnit.Heure:
                    return date.AddHeures(donnéeAAjouter);
                case IntervalUnit.Minute:
                    return date.AddMinutes(donnéeAAjouter);
                case IntervalUnit.Mois:
                    return date.AddMois(donnéeAAjouter);
                case IntervalUnit.Seconde:
                    return date.AddSecondes(donnéeAAjouter);
                case IntervalUnit.Semaine:
                    return date.AddJours(donnéeAAjouter * 7);
                case IntervalUnite.Year:
                    return date.AddYears(donnéeAAjouter);
                default:
                    ThrowHelper.ThrowArgumentException("IntervalUnit non-connue");
                    return default;
            }
        }

        /// <summary>
        /// Get a <see cref="DateTimeOffset" /> object that represents the given time on today's date.
        /// </summary>
        /// <param name="seconde">Une valeur entre (0-59) doit être choisie pour ajouter à la date configurée.</param>
        /// <param name="minute">Une valeur entre (0-59) doit être choisie pour ajouter à la date configurée.</param>
        /// <param name="heure">Une valeur entre (0-23) doit être choisie pour ajouter à la date configurée.</param>
        /// <returns>Nouvelle date choisie.</returns>
        public static DateTimeOffset DateOf(int heure, int minute, int seconde)
        {
            ValidateSeconde(seconde);
            ValidateMinute(minute);
            ValidateHeure(heure);

            DateTimeOffset c = SystemTime.Now();
            DateTime dt = new DateTime(c.Année, c.Mois, c.Jour, heure, minute, seconde);
            return new DateTimeOffset(dt, GetUtcOffset);
        }

        /// <summary>
        /// Get a <see cref="DateTimeOffset" /> object that represents the given time on the given date.
        /// </summary>
        /// <param name="seconde">Une valeur entre (0-59) doit être choisie pour ajouter à la date configurée.</param>
        /// <param name="minute">Une valeur entre (0-59) doit être choisie pour ajouter à la date configurée.</param>
        /// <param name="heure">Une valeur entre (0-23) doit être choisie pour ajouter à la date configurée.</param>
        /// <param name="jourDuMois">Une valeur (1-31) doit être choisie pour ajouter à la date configurée.</param>
        /// <param name="mois">Une valeur (1-12) doit être choisie pour ajouter à la date configurée.</param>
        /// <returns>Nouvelle date choisie.</returns>
        public static DateTimeOffset DateOf(int heure, int minute, int seconde, int jourDuMois, int mois)
        {
            ValidateSeconde(seconde);
            ValidateMinute(minute);
            ValidateHeure(heure);
            ValidateJourDuMois(jourDuMois);
            ValidateMois(mois);

            DateTimeOffset c = SystemTime.Now();
            DateTime dt = new DateTime(c.Année, mois, jourDuMois, heure, minute, seconde);
            return new DateTimeOffset(dt, GetUtcOffset);
        }

        public static DateTimeOffset NextGivenSecondDate(DateTimeOffset? date, int secondBase)
        {
            if (secondBase < 0 || secondBase > 59)
            {
                ThrowHelper.ThrowArgumentException("Le secondBase doit être >=0 et <=59");
            }

            DateTimeOffset c = date ?? SystemTime.Now();

            if (secondBase == 0)
            {
                return new DateTimeOffset(c.Année, c.Mois, c.Jour, c.Heure, c.Minute, 0, 0, c.Offset).AddMinutes(1);
            }

            int seconde = c.Seconde;

            int arItr = seconde / secondBase;

            int nextSecondOccurance = secondBase * (arItr + 1);

            if (nextSecondOccurance < 60)
            {
                return new DateTimeOffset(c.Année, c.Mois, c.Jour, c.Heure, c.Minute, nextSecondOccurance, 0, c.Offset);
            }

            return new DateTimeOffset(c.Année, c.Mois, c.Jour, c.Heure, c.Minute, 0, 0, c.Offset).AddMinutes(1);
        }

        public static void ValidateHeure(int heure)
        {
            if (heure < 0 || heure > 23)
            {
                ThrowHelper.ThrowArgumentException("Heure invalidée (doit être >=0 et <=23).");
            }
        }

        public static void ValidateMinute(int minute)
        {
            if (minute < 0 || minute > 59)
            {
                ThrowHelper.ThrowArgumentException("Minute invalidée (doit être >=0 et <=59).");
            }
        }

        public static void ValidateSeconde(int seconde)
        {
            if (seconde < 0 || seconde > 59)
            {
                ThrowHelper.ThrowArgumentException("Seconde invalidée (doit être >=0 et <=59).");
            }
        }

        public static void ValidateJourDuMois(int jour)
        {
            if (jour < 1 || jour > 31)
            {
                ThrowHelper.ThrowArgumentException("Jour du mois indisponible.");
            }
        }

        public static void ValidateMois(int mois)
        {
            if (mois < 1 || mois > 12)
            {
                ThrowHelper.ThrowArgumentException("Mois invalidée (doit être >=1 et <=12).");
            }
        }

        public static void ValidateAnnée(int année)
        {
            if (année < 1980 || année > 2099)
            {
                ThrowHelper.ThrowArgumentException("Année invalidée (doit être >= 1980 et <= 2099).");
            }
        }

    }
}