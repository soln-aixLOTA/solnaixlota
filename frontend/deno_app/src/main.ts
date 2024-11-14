import { Application, Router } from "https://deno.land/x/oak/mod.ts";
import { chatbot } from "./modules/chatbot.ts";

const app = new Application();
const router = new Router();

router.get("/", (context) => {
    context.response.body = "Welcome to the Deno Frontend!";
});

router.post("/chatbot", chatbot);

app.use(router.routes());
app.use(router.allowedMethods());

await app.listen({ port: 8000 }); 