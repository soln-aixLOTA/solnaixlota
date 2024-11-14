import { Router } from "https://deno.land/x/oak@v12.5.0/mod.ts";

export const router = new Router();

router.get("/health", (context) => {
  context.response.body = { status: "OK" };
});

// Add more routes as needed
router.get("/", (context) => {
  context.response.body = "Welcome to the Deno Application!";
});
  