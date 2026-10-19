package com.acme.notifications

data class Message(val recipient: String, val subject: String, val body: String)

interface Notifier {
    val channel: String

    fun send(message: Message): Boolean

    fun supports(recipient: String): Boolean = recipient.isNotBlank()
}

fun Message.preview(maxLength: Int = 40): String =
    if (body.length <= maxLength) body else body.take(maxLength) + "…"
