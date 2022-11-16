module.exports = {
  content: ['../**/*.html'],
  darkMode: 'class',
  theme: {
    container: {
      center: true,
      padding: {
        DEFAULT:'2rem',
        sm: '2rem',
        lg: '4rem',
        xl: '8rem',
        '2xl': '10rem',
      },
    },
    extend: {
      colors: {
        gray: {
          700:'#363636',
          800: '#292929',
          900: '#1a1a1a',
        },
      },
    },
  },
  plugins: [],
};
