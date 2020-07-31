<template>
  <div id="app">
    <router-view/>
  </div>
</template>

<script>
export default {
  data: () => ({
    err: false,
  }),

  errorCaptured(err, vm, info) {
    console.log(`出现错误: ${info}`);
    this.$router.back();
    return false;
  },
}
</script>
