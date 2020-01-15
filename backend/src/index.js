const Router = require("koa-router");
const Koa = require("koa");
const bodyParser = require("koa-bodyparser");

const api = require("./api");

const app = new Koa();
const router = new Router();

app.use(bodyParser());

router.use("/api", api.routes());

app.use(router.routes()).use(router.allowedMethods());
app.listen(4000, () => {
  console.log("start");
});
