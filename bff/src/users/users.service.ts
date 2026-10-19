import { Injectable } from "../decorators";
import { UpstreamClient } from "../http/upstream";

export interface UserSummary {
  id: string;
  name: string;
  status: string;
}

@Injectable()
export class UsersService {
  constructor(private readonly upstream: UpstreamClient) {}

  list(): Promise<UserSummary[]> {
    return this.upstream.get<UserSummary[]>("/users");
  }

  get(id: string): Promise<UserSummary> {
    return this.upstream.get<UserSummary>(`/users/${id}`);
  }

  create(body: Partial<UserSummary>): Promise<UserSummary> {
    return this.upstream.post<UserSummary>("/users", body);
  }
}
