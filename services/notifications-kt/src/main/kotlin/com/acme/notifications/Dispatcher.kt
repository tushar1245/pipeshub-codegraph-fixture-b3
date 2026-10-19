package com.acme.notifications

object Dispatcher {
    private val notifiers = mutableListOf<Notifier>()

    fun register(notifier: Notifier) {
        notifiers += notifier
    }

    fun dispatch(message: Message): Int =
        notifiers.count { it.supports(message.recipient) && it.send(message) }
}

fun defaultDispatcher(sender: String): Dispatcher {
    Dispatcher.register(EmailNotifier(sender))
    return Dispatcher
}

fun main() {
    val dispatcher = defaultDispatcher("noreply@acme.test")
    val sent = dispatcher.dispatch(Message("ada@acme.test", "Order shipped", "Your order is on its way."))
    println("sent=$sent")
}
