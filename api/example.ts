export default (request: Request) => {
  return new Response(`Hello, from ${request.url}!`);
};