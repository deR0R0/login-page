/** @type {import('tailwindcss').Config} */
module.exports = {
  content: ["./frontend/index.html", "./frontend/signup/index.html", "./frontend/home/index.html"],
  theme: {
    extend: {
      fontFamily: {
        inter: ["Inter", '-apple-system', 'sans-serif'],
        mono: ["Roboto Mono", '-apple-system', 'serif']
      },
    },
  },
  plugins: [],
}