class Deploy {
    String env;
    List<String> services = [];

    void rollout() {
        for (String name : services) {
            if (healthy(name)) {
                println("deploying ${name} to ${env}")
            } else {
                println("skipping ${name}: health check failed")
            }
        }
    }

    boolean healthy(String name) {
        return name && !name.contains(' ')
    }
}
