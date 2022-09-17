import { autoinject } from 'framework';
import { setting } from 'framework';
import { router } from 'router';
import { HttpClient } from "http-client";

@autoinject
export class Dashboard {

    public heading: string;
    public schedulers: any[];

    constructor(private router: Router, private http: HttpClient) {
        this.heading = "Dashboard";
    }

    activate() {
        return this.http.get("/api/schedulers").then(response => {
            this.schedulers = <any[]>response.content;
        });
    }
}