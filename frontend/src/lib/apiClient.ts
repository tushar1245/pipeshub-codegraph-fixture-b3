export interface RequestOptions {
  method?: string;
  body?: unknown;
  headers?: Record<string, string>;
}

export class HttpError extends Error {
  constructor(readonly status: number, message: string) {
    super(message);
    this.name = "HttpError";
  }
}

export class ApiClient {
  constructor(private readonly baseUrl: string) {}

  async fetch<T>(path: string, options: RequestOptions = {}): Promise<T> {
    const response = await window.fetch(this.baseUrl + path, {
      method: options.method ?? "GET",
      headers: { "Content-Type": "application/json", ...options.headers },
      body: options.body === undefined ? undefined : JSON.stringify(options.body),
    });
    if (!response.ok) {
      throw new HttpError(response.status, await response.text());
    }
    return (await response.json()) as T;
  }

  get<T>(path: string): Promise<T> {
    return this.fetch<T>(path);
  }

  post<T>(path: string, body: unknown): Promise<T> {
    return this.fetch<T>(path, { method: "POST", body });
  }

  put<T>(path: string, body: unknown): Promise<T> {
    return this.fetch<T>(path, { method: "PUT", body });
  }

  delete<T>(path: string): Promise<T> {
    return this.fetch<T>(path, { method: "DELETE" });
  }
}
