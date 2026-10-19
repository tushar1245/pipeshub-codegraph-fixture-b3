# frozen_string_literal: true

require_relative "base"

module Admin
  class User < Base
    EMAIL = /\A[^@\s]+@[^@\s]+\z/

    def validate
      errors << "email is invalid" unless EMAIL.match?(attributes[:email].to_s)
      errors << "name is required" if attributes[:name].to_s.strip.empty?
    end

    def display_name
      "#{attributes[:name]} <#{attributes[:email]}>"
    end
  end
end
