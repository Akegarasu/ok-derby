<template>
  <div>
    <base-header
      type="sb-info"
      class="pb-6 pb-8 pt-5 pt-md-8 background"
      style="height: calc(100vh + 6rem)"
      :style="{ 'background-image': `url(${backgroundImg})` }"
    >
    </base-header>

    <div class="container-fluid mt--7">
      <base-alert type="warning">
        <span class="alert-inner--icon">
          <i class="ni ni-lock-circle-open"></i>
        </span>
        <span class="alert-inner--text">
          <strong> 提示! </strong>
          本项目（ok-derby）以及核心（auto-derby）均采用 MIT License 开源。
        </span>
      </base-alert>
      <div class="row" style="margin-bottom: 10px">
        <div class="col-xl-8 mb-5 mb-xl-0">
          <FastUsing />
        </div>

        <div class="col-xl-4 md-5">
          <all-jobs />
        </div>
      </div>
      <div class="row" style="margin-bottom: 10px">
        <div class="col justify-content-center">
          <commandUsing />
        </div>
      </div>
      <div class="row" style="margin-bottom: 10px">
        <div class="col justify-content-center">
          <log />
        </div>
      </div>
      <div class="row">
        <div class="col justify-content-center">
          <div class="card">
            <div class="card-body">
              <base-progress
                type="info"
                :height="8"
                :value="40"
                label="开发进度"
              ></base-progress>
            </div>
          </div>
        </div>
      </div>
    </div>
  </div>
</template>
<script>

import BaseProgress from "../components/BaseProgress";
import FastUsing from "./components/FastUsing";
import commandUsing from "./components/CommandUsing";
import AllJobs from "./components/AllJobs";
import Log from "./components/Log";

export default {
  components: {
    BaseProgress,
    FastUsing,
    commandUsing,
    AllJobs,
    Log,
  },
  data() {
    return {};
  },
  watch: {},
  computed: {
    backgroundImg() {
      return require("../../public/img/mayano.jpeg");
    },
  },
  methods: {},
  mounted() {},
};
</script>
<style lang="scss">
.announce-link {
  color: #ffffff;
  transition: all 0.5s;
  text-decoration: underline;

  &:hover {
    text-decoration: underline;
    color: #5e72e4;
  }
}
</style>
