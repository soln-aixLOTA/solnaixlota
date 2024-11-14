import { Application } from "https://deno.land/x/oak/mod.ts";
import { router } from "./routes/mod.ts";
import { aiMiddleware } from "./middleware/ai.ts";

const app = new Application({
  router,
  middleware: [aiMiddleware],
});

app.listen({ port: 8000 });