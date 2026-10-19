package com.acme.notifications

class EmailNotifier(private val sender: String) : Notifier {
    override val channel: String = "email"

    override fun send(message: Message): Boolean {
        if (!supports(message.recipient)) return false
        println("[$channel] from=$sender to=${message.recipient}: ${message.preview()}")
        return true
    }

    override fun supports(recipient: String): Boolean = EMAIL.matches(recipient)

    companion object {
        private val EMAIL = Regex("^[^@\\s]+@[^@\\s]+$")
    }
}
