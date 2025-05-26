/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
    "./src/**/*.{js,jsx,ts,tsx}",
  ],
  theme: {
    extend: {
      colors: {
        'puebla-blue': '#1e40af',
        'puebla-gold': '#f59e0b',
      }
    },
  },
  plugins: [],
}
