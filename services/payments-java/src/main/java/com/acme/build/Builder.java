package com.acme.build;

public final class Builder {
    private final StringBuilder parts = new StringBuilder();

    private Builder() {
    }

    public static Builder create() {
        return new Builder();
    }

    public Builder add(String key, String value) {
        if (parts.length() > 0) {
            parts.append(", ");
        }
        parts.append(key).append('=').append(value);
        return this;
    }

    public String build() {
        return "{" + parts + "}";
    }

    public static String describe(String service, String implementation) {
        return create().add("service", service).add("impl", implementation).build();
    }
}
