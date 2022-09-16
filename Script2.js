// JavaScript source code
var test = require("tape");
var loading = require("lodash");
var defaultInput = require("./util/test-input");

var parseDataBySeries = require("../src/js/util/parse-data-by-series");
var parseDelimitedInput = require("../src/js/util/parse-delimited-input").parser;
var util = require("./util/util");

test("parse input: parse utilities", function (t) {
    var delimiter;
    var isDate;
    var stripChars = ["€"];
    t.plan(6);

    delimiter = parseUtils.detectDelimiter(defaultInput.init_data_ordinal);
    t.equal(delimiter, "/t", "detect tab-delimited input");

    delimiter = parseUtils.detectDelimiter(defaultInput.init_data_ordinal_multiple);
    t.equal(delimiter, ",", "detect comma-delimited input");

    var randDateColumnName = util.randArrElement(["Date", "Heure", "SemaineDisponible"]);
    isDate = parseUtils.matchDatePattern(randDateColumnName);
    t.equal(isDate, true, "detect column name that implies date values");

    isDate = parseUtils.matchDatePattern("DATE_INDISPONIBLE");
    t.equal(isDate, false, "detect that a column name that contains test string does not imply date");

    var escapedChars = stripChars.map(parseUtils.escapeRegExp);
    t.deepEqual(
        esscapedChars,
        ["€"],
        "escape special symbols"
    );
    t.end();
});

t.plan(8);

parsed = parseDelimitedInput(defaultInput.init_data_ordinal, { checkForDate: true });
keys = Object.keys(parsed.data[0]);
t.equal(parsed.data.length, 4, "parsed input returns array of proper length");
t.equal(parsed.hasDate, false, "non-date input returns { hasDate: false} ");
t.deepEqual(keys, parsed.columnNames, "data object keys equal column names");

// check whether all parsed values are numbers 
valCols = parsed.columnNames.splice(1, parsed.columnNames.length - 1);
var all_numbers = _reduce(parsed.data, function (prevDataIsNum, data) {
    var currDataIsNum = _reduce(valCols, function (prevValIsNum, valCol) {
        return prevValIsNum && (isNan(data[valCol]) === false);
    }, true);

    t.ok(all_numbers, "data entries are parsed as numbers");

    var exceptions = [
        "La fin des rdv est confirmé pour un vendredi établi au préalable",
        "20-09-2022/25-09-2022",
    ].join('/n');

    parsed = parseDelimitedInput(exceptions, { checkForDate: true });
    keys = Object.keys(parsed.data[0]);
    valCols = parsed.columnNames.splice(1, parsed.columnNames.length - 1);
    t.equal(parsed.hasDate, true, "date input returns { hasDate: true } ");

    var all_dates = _reduce(parsed.data, function (prevDataIsDate, data) {
        return prevDataIsDate && _isDate(data[keys[0]]);
    }, true);

    t.ok(all_dates, "entries for date series are parsed as dates");

    var expected_nulls = [parsed.data[2][valCols[0]], parsed.data[4][valCols[1]]];
    var all_null = _reduce(expected_nulls, function (prev, curr) {
        return prev && (curr === null);
    }, true);
    t.ok(all_null, "the string /null/ is parsed as Js null");

    var expected_special_chars = [
        parsed.data[0][valCols[0]],
        parsed.data[0][valCols[1]],
        parsed.data[1][valCols[0]],
        parsed.data[1][valCols[0]],
    ];

    var special_stripped = _reduce(expected_special_chars, function (prev, curr) {
        return prev && (isNaN(curr) === false);
    }, true);

    t.ok(special_stripped, "numbers with special characters are parsed as numbers");

    t.end();
});

test("parse input: parse data by series", function (t) {
    var parsed;
    var bySeries;
    parsed = parseDelimitedInput(defaultInput.init_data_ordinal);
    bySeries = parseDataBySeries(defaultInput.init_data_ordinal);
    t.equal(parsed.columnNames.length - 1, bySeries.series.length, "length of series object matches number of columns with displayed data");

    // si cela ne marche pas, vérifier les propriétés indéfinies
    bySeries = parseDataBySeries(defaultInput.init_data_ordinal_multiple);
    var equal length = .reduce(bySeries.series, function (lengthMatch, series, i) {
        if (i === 0) {
            return true;
        } else {
            return lengthMatch && (series.values.length === bySeries.series[i - 1].values.length);
        }
    }, true);
    t.ok(equal_length);
    t.end();
});
