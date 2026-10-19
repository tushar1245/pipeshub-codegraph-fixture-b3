# Architecture

Requests enter through the BFF (`bff/`), which calls the Python API.
Each backend domain follows routes -> service -> repository -> database.
Domain events are published on the in-process `EventBus` and picked up
by the Node worker through the queue.

Pricing discounts are computed natively in `services/pricing-rs` and
exposed to Python as the `pricing_native` extension module.
