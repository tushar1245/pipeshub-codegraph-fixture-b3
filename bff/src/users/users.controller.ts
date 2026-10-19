import { Controller, Get, Post } from "../decorators";
import { clamp } from "../util/clamp";
import { UsersService, type UserSummary } from "./users.service";

@Controller("users")
export class UsersController {
  constructor(private readonly users: UsersService) {}

  @Get()
  async list(limit = 20): Promise<UserSummary[]> {
    const all = await this.users.list();
    return all.slice(0, clamp(limit, 1, 100));
  }

  @Get(":id")
  show(id: string): Promise<UserSummary> {
    return this.users.get(id);
  }

  @Post()
  create(body: Partial<UserSummary>): Promise<UserSummary> {
    return this.users.create(body);
  }
}
