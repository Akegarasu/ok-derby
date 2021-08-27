<template>
  <div class="card">
    <div class="card-header">
      <div class="row align-items-center">
        <div class="col">
          <h3 class="mb-0">可用任务</h3>
        </div>
      </div>
    </div>
    <div class="card-body">
      <badge
        v-for="tag in tags"
        tag="a"
        :key="tag.name"
        @click.native="rua(tag.name)"
        href="javascript:void(0)"
        type="info"
        >{{ tag.name }}</badge
      >
    </div>
  </div>
</template>

<script>
import CONFIG from "@/config.json";
export default {
  name: "AllJobs",
  props: {},
  data() {
    return {
      tags: CONFIG.availableJobs,
    };
  },
  methods: {
    rua(t) {
      this.$notify({
        type: "info",
        title: "任务详情",
        message: t,
        timeout: 1000
      });
    },
  },
};
</script>

<style></style>
