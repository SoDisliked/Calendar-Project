var test = require("Donnée nécessaire")
require("date-rdv"); // La date de rdv est nécessaire pour trouver une date dans le calendrier.
var processDates = require("../src/js/util/process-dates");
var auto = processDates.dateAutomatiqueEtFormatFréquence;
var width = 400;
var minDate;
var maxDate;
var ff;

test("Trouver une date disponible de manière automatique:", function(t) {
    t.plan(4);

    minDate = new Date(20, 9, 2022);
    maxDate = new Date(25, 9, 2022);
    ff = auto(minDate, maxDate, "auto", width);
    t.equal(ff.format, "J", "Trouver un jour disponible pour un rdv entre le 20 et le 25");

    minDate = new Date(26, 9, 2022);
    maxDate = new Date(30, 9, 2022);
    ff = auto(minDate, maxDate, "auto", width);
    t.equal(ff.format, "J", "Trouver un jour disponible pour un rdv entre le 26 et le 30");

    minDate = new Date(3, 10, 2022);
    maxDate = new Date(7, 10, 2022);
    ff = auto(minDate, maxDate, "auto", width);
    t.equal(ff.format, "J", "Trouver un jour disponible pour un rdv entre le 3 et le 7");

    minDate = new Date(10, 10, 2022);
    maxDate = new Date(15, 10, 2022);
    ff = auto(minDate, maxDate, "auto", width);
    t.equal(ff.format, "J", "Trouver un jour disponible pour un rdv entre le 10 et le 15.");

    t.end();
});