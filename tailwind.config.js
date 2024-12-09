// tailwind.config.mjs
export default {
  content: [
    "./app.vue",
    "./pages/**/*.vue",
    "./components/**/*.vue",
    "./layouts/**/*.vue",
    "./plugins/**/*.js",
    "./nuxt.config.{js,ts}"
  ],
  theme: {
    extend: {
      fontFamily: {
        roboto: ["'Roboto Mono'", 'sans-serif'], 
        quicksand: ['Quicksand', 'sans-serif'],
        press: ["'Press Start 2P'", 'cursive'],
      },
    },
  },
  plugins: [],
};
