# frozen_string_literal: true

require_relative "../../lib/admin/user"

RSpec.describe Admin::User do
  it "rejects a malformed email" do
    user = described_class.new(name: "Ada", email: "ada")
    expect(user.save).to be(false)
    expect(user.errors).to include("email is invalid")
  end

  it "saves a valid user" do
    user = Admin::User.new(name: "Ada", email: "ada@acme.test")
    expect(user.save).to be(true)
  end
end
