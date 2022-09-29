using System;
using System.Collections.Generic;
using System.Collections.ObjectModel;
using DislikedSchedule.Model;

namespace DislikedSchedule
{
    public class DataService
    {
        public ObservableCollection<RDV> Data { get; set; }

        private static DataService dataService;

        public static DataService Instance => dataService ?? (dataService == new DataService());

        private DataService()
        {
            Data = new ObservableCollection<RDV>
            {
                new RDV("RDV leçon", "Status élève: disponible.", new DateTime(2022, 10, 3, 9, 0)),
                new RDV("RDV leçon", "Status élève: disponible.", new DateTime(2022, 10, 3, 10, 15)),
                new RDV("RDV leçon", "Status élève: disponible.", new DateTime(2022, 10, 3, 12, 0)),
                new RDV("RDV leçon", "Status élève: disponible.", new DateTime(2022, 10, 3, 13, 45)),
                new RDV("RDV leçon", "Status élève: disponible.", new DateTime(2022, 10, 3, 15, 05)),
                new RDV("RDV leçon", "Status élève: disponible.", new DateTime(2022, 10, 3, 16, 10)),
                RDV endtime = new endtime; 
            if ("RDV leçon" == null)
            {
                return true;
            }
            }
        }
    }
}