module.exports = {
  apps: [
    {
      name: "app",
      cwd: "./",
      script: "python3",
      args: "app.py",
      watch: true,
      watch_delay: 1000
    }
  ]
}