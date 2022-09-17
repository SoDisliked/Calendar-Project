﻿import { Router } from "framework";

export class App {
    private router: Router;

    configureRouter(config, router: Router) {
        config.title = "Web Console";
        config.map([
            { route: ["", "dashboard"], moduleId: "views/dashboard", nav: true, title: "Dashboard" },
            { route: ["schedulers/:schedulerName:"], name: "scheduler-details", moduleId: "views/scheduler-router", nav: false, title: "Scheduler Details" }
        ]);
        this.router = router;
    }
}