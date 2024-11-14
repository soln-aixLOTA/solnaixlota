import { Application, Router } from "https://deno.land/x/oak@v12.5.0/mod.ts";
import { chatbot } from "./modules/chatbot.ts";
import { aiMiddleware } from "./middleware/ai.ts";

const app = new Application();
const router = new Router();

router.get("/", (context) => {
    context.response.body = "Welcome to the Deno Frontend!";
});

router.post("/chatbot", chatbot);

app.use(aiMiddleware);
app.use(router.routes());
app.use(router.allowedMethods());

await app.listen({ port: 8000 }); 