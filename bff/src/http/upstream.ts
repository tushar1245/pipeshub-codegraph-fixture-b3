export class UpstreamError extends Error {
  constructor(readonly status: number, readonly path: string) {
    super(`upstream ${path} answered ${status}`);
  }
}

export class UpstreamClient {
  constructor(private readonly baseUrl: string) {}

  async get<T>(path: string): Promise<T> {
    return this.send<T>("GET", path);
  }

  async post<T>(path: string, body: unknown): Promise<T> {
    return this.send<T>("POST", path, body);
  }

  private async send<T>(method: string, path: string, body?: unknown): Promise<T> {
    const response = await fetch(this.baseUrl + path, {
      method,
      headers: { "content-type": "application/json" },
      body: body === undefined ? undefined : JSON.stringify(body),
    });
    if (!response.ok) {
      throw new UpstreamError(response.status, path);
    }
    return (await response.json()) as T;
  }
}
