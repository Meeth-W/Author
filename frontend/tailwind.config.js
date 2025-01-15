module.exports = {
  content: ["./index.html", "./src/**/*.{js,ts,jsx,tsx}"],
  theme: {
    extend: {
      colors: {
        aqua: {
          400: "#00FFFF",
          500: "#00E5FF",
          600: "#00BFFF",
        },
      },
      animation: {
        fadeIn: "fadeIn 0.8s ease-in-out",
        slideIn: "slideIn 0.5s ease-out",
      },
      keyframes: {
        fadeIn: {
          from: { opacity: 0 },
          to: { opacity: 1 },
        },
        slideIn: {
          from: { transform: "translateX(-100%)", opacity: 0 },
          to: { transform: "translateX(0)", opacity: 1 },
        },
      },
    },
  },
  plugins: [],
};
