# frozen_string_literal: true

module Admin
  def self.store
    @store ||= []
  end

  class Base
    attr_reader :attributes, :errors

    def initialize(attributes = {})
      @attributes = attributes.transform_keys(&:to_sym)
      @errors = []
    end

    def save
      validate
      return false unless errors.empty?

      persist
      true
    end

    def validate; end

    def to_h
      attributes.dup
    end

    private

    def persist
      Admin.store << to_h
    end
  end
end
