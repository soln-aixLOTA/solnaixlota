import { Application } from "https://deno.land/x/oak@v12.5.0/mod.ts";
import { router } from "./routes/mod.ts";
import { aiMiddleware } from "./middleware/ai.ts";

const app = new Application();
app.use(aiMiddleware);
app.use(router.routes());
app.use(router.allowedMethods());

app.listen({ port: 8000 });