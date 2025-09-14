/** @type {import('tailwindcss').Config} */
module.exports = {
  content: [
      './apps/**/*.{html,js,py}',
      './templates/**/*.html',
  ],
  theme: {
    extend: {
      colors: {
        primary: '#0EA5E9',
        secondary: '#8B5CF6',
        accent: '#06FFA5',
        dark: '#0F172A',
        surface: '#1E293B',
        glass: 'rgba(255, 255, 255, 0.1)',
      }
    },
  },
  plugins: [],
}
