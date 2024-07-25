import { fileURLToPath, URL } from 'node:url'

import { defineConfig } from 'vite'
import vue from '@vitejs/plugin-vue'

// https://vitejs.dev/config/
export default defineConfig({
  server : {
    port : 5173, 
    proxy: {
      "/api": {
        target: "https://imaginecx--tst2.custhelp.com",
        secure : true,
        headers : {        "Access-Control-Allow-Origin": "*",
          "Access-Control-Allow-Methods": "POST, GET, PUT",
          "Authorization": "Basic " + "SUNYQ2FuZGlkYXRlOldlbGNvbWUyMDI0"},
        changeOrigin: true,
        rewrite: (path) => path.replace(/^\/api/, ""),
      },
    },
  },
  plugins: [
    vue(),
  ],
  resolve: {
    alias: {
      '@': fileURLToPath(new URL('./src', import.meta.url))
    }
  }
})
