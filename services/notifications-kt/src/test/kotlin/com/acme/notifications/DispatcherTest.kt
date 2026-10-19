package com.acme.notifications

import kotlin.test.Test
import kotlin.test.assertEquals

class DispatcherTest {
    private class RecordingNotifier : Notifier {
        val sent = mutableListOf<Message>()
        override val channel = "test"
        override fun send(message: Message): Boolean = sent.add(message)
    }

    @Test
    fun dispatchesToSupportingNotifiers() {
        val notifier = RecordingNotifier()
        Dispatcher.register(notifier)
        val delivered = Dispatcher.dispatch(Message("ada@acme.test", "Hi", "Hello"))
        assertEquals(1, delivered)
        assertEquals("Hello", notifier.sent.single().body)
    }
}
