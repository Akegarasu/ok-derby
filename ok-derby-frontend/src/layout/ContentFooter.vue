<template>
  <footer class="footer px-4">
    <div class="row align-items-center justify-content-lg-between">
      <div class="col-lg-6">
        <div class="copyright text-center text-lg-left text-muted">
          © {{year}} <a href="https://anzu.link" class="font-weight-bold ml-1" target="_blank">秋葉</a>
        </div>
      </div>
      <div class="col-lg-6">
        <ul class="nav nav-footer justify-content-center justify-content-lg-end">
          <li class="nav-item">
            <a href="https://github.com/Akegarasu/ok-derby" class="nav-link" target="_blank">关于</a>
          </li>
          <li class="nav-item">
            <a href="https://anzu.link" class="nav-link" target="_blank">Blog</a>
          </li>
          <li class="nav-item">
            <a href="https://github.com/Akegarasu/ok-derby/blob/main/LICENSE" class="nav-link" target="_blank">License</a>
          </li>
        </ul>
      </div>
    </div>
  </footer>
</template>
<script>
export default {
  data() {
    return {
      year: new Date().getFullYear()
    };
  }
};
</script>
<style></style>
