# frozen_string_literal: true

require "csv"
require_relative "user"

module Admin
  class Exporter
    HEADERS = %w[name email].freeze

    def initialize(users)
      @users = users
    end

    def to_csv
      CSV.generate do |csv|
        csv << HEADERS
        valid_users.each { |user| csv << user.to_h.values_at(:name, :email) }
      end
    end

    def valid_users
      @users.select(&:save)
    end

    def self.export(rows)
      new(rows.map { |row| User.new(row) }).to_csv
    end
  end
end
