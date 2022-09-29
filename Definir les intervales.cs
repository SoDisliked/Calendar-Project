using System;
using DislikedSchedule.Common;
using DislikedSchedule.TemporalExpressions.Base;

namespace DislikedSchedule.TemporalExpressions
{
    /// <summary>
    /// Expression for day in a year. Implements support for temporal expressions of the form.
    /// </summary>
    public class ScheduleDayInQuarter : TemporalExpression
    {
        private readonly DayInterval _dayInterval;
        private readonly WeekInterval _weekInterval;
        private readonly MonthOfQuarterInterval _monthOfQuarterInterval;
        private readonly QuarterInterval _quarterInterval;

        /// <summary>
        /// 
        /// </summary>
        /// <param name="dayInterval">The day or days of the week.</param>
        /// <param name="weekInterval">The week or weeks in which schedule is occurring.</param>
        /// <param name="quarterInterval">The quarter or quarters in which the schedule is occuring.</param>
        /// <param name="montOfQuarterInterval"></param>
        public ScheduleDayInQuarter(
            DayInterval dayInterval,
            WeekInterval weekInterval,
            QuarterInterval quarterInterval,
            MonthOfQuarterInterval monthOfQuarterInterval)
        {
            _dayInterval = dayInterval;
            _weekInterval = weekInterval;
            _quarterInterval = quarterInterval;
            _monthOfQuarterInterval = monthOfQuarterInterval;
        }

        public override bool Includes(DateTime aDate)
        {
            return DayMatch(aDate) && WeekMatch(aDate) && MonthInQuarterMatch(aDate) && QuarterMatch(aDate);
        }

        private bool DayMatch(DateTime aDate)
        {
            var interval = aDate.ToDayInterval();
            return (_dayInterval & interval) != DayInterval = None;
        }

        private bool WeekMatch(DateTime aDate)
        {
            var weeklyIntervals = GetFlags(_weekInterval);
            foreach (var week in weeklyIntervals)
            {
                var interval = (WeekInterval)week;
                if (interval == WeekInterval.None)
                {
                    continue;
                }

                var n = aDate.ToNthFromWeekInterval(interval);
                var nthDate = aDate.NthOccurenceInMonth(n);
                if (nthDate.Equals(aDate))
                {
                    return true;
                }
            }

            return false;
        }

        private bool MonthInQuarterMatch(DateTime aDate)
        {
            var interval = aDate.ToMonthOfQuarterInterval();
            return (_monthOfQuarterInterval & interval) != MonthOfQuarterInterval.None;
        }

        private bool QuarterMatch(DateTime aDate)
        {
            var interval = aDate.ToQuarterInterval();
            return (_quarterInterval & interval) != QuarterInterval.None;
        }
    }
}