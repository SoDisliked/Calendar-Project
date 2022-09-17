export function configure(Logiciel) {
    logiciel.use
        .standardConfiguration()
        .developmentLogging()
        .feature("resources");

    logiciel.start().then(a => a.setRoot("views/logiciel"))
}