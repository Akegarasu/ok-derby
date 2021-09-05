<template>
  <div>
    <base-header
      class="header pb-8 pt-5 pt-lg-8 d-flex align-items-center"
      style="
        min-height: 600px;
        background-image: url(img/theme/profile-cover.jpg);
        background-size: cover;
        background-position: center top;
      "
    >
      <!-- Mask -->
      <span class="mask bg-gradient-success opacity-8"></span>
      <!-- Header container -->
      <div class="container-fluid d-flex align-items-center">
        <div class="row">
          <div class="col-lg-12 col-md-10">
            <h1 class="display-2 text-white">朴实无华的设置页</h1>
            <p class="text-white mt-0 mb-5">
              此处为高级设置，普通用户请勿随意更改
            </p>
            <a
              href="https://github.com/Akegarasu/ok-derby/"
              class="btn btn-info"
              >查看帮助</a
            >
          </div>
        </div>
      </div>
    </base-header>

    <div class="container-fluid mt--7">
      <div class="row">
        <div class="col-xl-4 order-xl-2 mb-5 mb-xl-0">
          <div class="card card-profile shadow">
            <div class="row justify-content-center">
              <div class="col-lg-3 order-lg-2">
                <div class="card-profile-image">
                  <a href="#">
                    <img
                      src="img/theme/riceshower.png"
                      class="rounded-circle"
                    />
                  </a>
                </div>
              </div>
            </div>
            <div
              class="card-header text-center border-0 pt-8 pt-md-4 pb-0 pb-md-4"
            >
              <div class="d-flex justify-content-between">
                <a
                  href="https://github.com/Akegarasu/ok-derby/issues"
                  class="btn btn-sm btn-info"
                  >反馈bug</a
                >
              </div>
            </div>
            <div class="card-body pt-0 pt-md-4">
              <div class="row">
                <div class="col">
                  <div
                    class="card-profile-stats d-flex justify-content-center mt-md-5"
                  >
                    <div>
                      <span class="heading">{{ version.AUTO_DERBY }}</span>
                      <span class="description">auto-derby版本</span>
                    </div>
                    <div>
                      <span class="heading">{{
                        version.OK_DERBY_FRONTEND
                      }}</span>
                      <span class="description">ok-derby前端版本</span>
                    </div>
                    <div>
                      <span class="heading">{{
                        version.OK_DERBY_BACKEND
                      }}</span>
                      <span class="description">ok-derby后端版本</span>
                    </div>
                  </div>
                </div>
              </div>
              <div class="text-center">
                <hr class="my-4" />
                <p>
                  还在努力开发中哟！
                </p>
                <a href="https://github.com/Akegarasu/ok-derby">ok-derby </a>
                <a href="https://github.com/NateScarlet/auto-derby"
                  >auto-derby</a
                >
              </div>
            </div>
          </div>
        </div>

        <div class="col-xl-8 order-xl-1">
          <card shadow type="secondary">
            <div slot="header" class="bg-white border-0">
              <div class="row align-items-center">
                <div class="col-8">
                  <h3 class="mb-0">设定</h3>
                </div>
                <div class="col-4 text-right">
                  <base-button size="sm" type="danger" @click="forceReset()">
                    强制重置
                  </base-button>
                  <base-button size="sm" type="primary" @click="saveSettings()">
                    保存（未做更改的不变）
                  </base-button>
                </div>
              </div>
            </div>
            <template>
              <form @submit.prevent>
                <h6 class="heading-small text-muted mb-4">通用设定</h6>
                <div class="pl-lg-4">
                  <div class="row">
                    <div class="col-lg-6">
                      <base-input
                        alternative=""
                        label="ADB连接地址(填写则启用adb模式)"
                        placeholder="ADB_ADDRESS"
                        input-classes="form-control-alternative"
                        v-model="model.ADB_ADDRESS"
                      />
                    </div>
                    <!-- <div class="col-lg-6">
                      <base-input
                        alternative=""
                        label="插件"
                        placeholder="PLUGINS"
                        input-classes="form-control-alternative"
                        v-model="model.PLUGINS"
                      />
                    </div> -->
                  </div>

                  <div class="row">
                    <div class="col-lg-6">
                      <base-input
                        alternative=""
                        label="OCR图像路径"
                        placeholder="ocr_image_path"
                        input-classes="form-control-alternative"
                        v-model="model.ocr_image_path"
                      />
                    </div>

                    <div class="col-lg-6">
                      <base-input
                        alternative=""
                        label="OCR数据路径"
                        placeholder="ocr_data_path"
                        input-classes="form-control-alternative"
                        v-model="model.ocr_data_path"
                      />
                    </div>
                  </div>

                  <div class="row" style="margin-bottom: 10px">
                    <div class="col justify-content-center">
                      <div class="card">
                        <div class="card-header">
                          <div class="row align-items-center">
                            <div class="col">
                              <h3 class="mb-0">可选项</h3>
                            </div>
                          </div>
                        </div>
                        <div class="card-body">
                          <div class="row">
                            <div class="col">
                              禁用OCR询问（会被插件覆盖）
                            </div>
                            <div class="col">
                              <base-switch v-model="model.ocr_prompt_disabled">
                              </base-switch>
                            </div>
                          </div>
                          <div class="row">
                            <div class="col">
                              使用旧的截图模式
                            </div>
                            <div class="col">
                              <base-switch
                                v-model="model.use_legacy_screenshot"
                              >
                              </base-switch>
                            </div>
                          </div>
                        </div>
                      </div>
                    </div>
                  </div>
                </div>

                <hr class="my-4" />

                <h6 class="heading-small text-muted mb-4">单人模式</h6>
                <div class="pl-lg-4">
                  <div class="row">
                    <div class="col-lg-6">
                      <base-input
                        alternative=""
                        label="训练等级目标(速,耐,力,根,智)"
                        placeholder="single_mode_target_training_levels"
                        input-classes="form-control-alternative"
                        v-model="model.single_mode_target_training_levels"
                      />
                    </div>
                    <div class="col-lg-6">
                      <base-input
                        alternative=""
                        label="比赛名次低于设定时暂停"
                        placeholder="pause_if_race_order_gt"
                        input-classes="form-control-alternative"
                        v-model="model.pause_if_race_order_gt"
                      />
                    </div>
                  </div>
                  <div class="row">
                    <div class="col-lg-6">
                      <base-input
                        alternative=""
                        label="比赛数据路径"
                        placeholder="single_mode_race_data_path"
                        input-classes="form-control-alternative"
                        v-model="model.single_mode_race_data_path"
                      />
                    </div>
                    <div class="col-lg-6">
                      <base-input
                        alternative=""
                        label="对话选项路径"
                        placeholder="single_mode_choice_path"
                        input-classes="form-control-alternative"
                        v-model="model.single_mode_choice_path"
                      />
                    </div>
                  </div>
                </div>
                <!-- <hr class="my-4" />
                <h6 class="heading-small text-muted mb-4">
                  Contact information
                </h6>
                <div class="pl-lg-4">
                  <div class="row">
                    <div class="col-md-12">
                      <base-input
                        alternative=""
                        label="Address"
                        placeholder="Home Address"
                        input-classes="form-control-alternative"
                        v-model="model.address"
                      />
                    </div>
                  </div>
                  <div class="row">
                    <div class="col-lg-4">
                      <base-input
                        alternative=""
                        label="City"
                        placeholder="City"
                        input-classes="form-control-alternative"
                        v-model="model.city"
                      />
                    </div>
                    <div class="col-lg-4">
                      <base-input
                        alternative=""
                        label="Country"
                        placeholder="Country"
                        input-classes="form-control-alternative"
                        v-model="model.country"
                      />
                    </div>
                    <div class="col-lg-4">
                      <base-input
                        alternative=""
                        label="Postal code"
                        placeholder="Postal code"
                        input-classes="form-control-alternative"
                        v-model="model.zipCode"
                      />
                    </div>
                  </div>
                </div>
                <hr class="my-4" />-->
                <!-- Description -->
                <!-- <h6 class="heading-small text-muted mb-4">About me</h6>
                <div class="pl-lg-4">
                  <div class="form-group">
                    <base-input alternative="" label="About Me">
                      <textarea
                        rows="4"
                        class="form-control form-control-alternative"
                        placeholder="A few words about you ..."
                      ></textarea>
                    </base-input>
                  </div>
                </div> -->
              </form>
            </template>
          </card>
        </div>
      </div>
    </div>
  </div>
</template>
<script>
import axios from "axios";
import CONFIG from "@/config.json";

export default {
  name: "settings",
  data() {
    return {
      version: {
        OK_DERBY_FRONTEND: "0.4",
        OK_DERBY_BACKEND: "0.4",
        AUTO_DERBY: "1.3",
      },
      model: {
        ADB_ADDRESS: "", // ADB Address
        // PLUGINS:
        //   storage.get("onPlugins") == undefined ? "" : storage.get("onPlugins"), // Plugins
        use_legacy_screenshot: "",
        ocr_data_path: "",
        ocr_image_path: "",
        ocr_prompt_disabled: "",
        // 单人模式
        single_mode_target_training_levels: "", // 训练目标
        pause_if_race_order_gt: "", // 暂停条件
        single_mode_race_data_path: "",
        single_mode_choice_path: "",
      },
      defaultSettings: {},
      backupSettings: {},
      changedSettings: {},
    };
  },
  methods: {
    // TODO: 将是否更改放入后端判断，而非前端
    loadConfig() {
      axios.get(CONFIG.backend + "/api/settings").then((response) => {
        this.model = JSON.parse(response.data.data);
        console.log(this.model);
        this.backupSettings = JSON.parse(JSON.stringify(this.model));
        this.defaultSettings = JSON.parse(JSON.stringify(this.model));
      });
    },
    checkChanged() {
      for (let key of Object.keys(this.model)) {
        if (this.model[key] !== this.backupSettings[key]) {
          this.changedSettings[key] = this.model[key];
        }
      }
      console.log(Object.keys(this.changedSettings).length);
      console.log(this.changedSettings);
    },
    forceReset() {
      axios
        .get(CONFIG.backend + "/api/settings/reset")
        .then((response) => {
          if (response.data.code == 0) {
            this.$notify({
              type: "info",
              title: `重置成功`,
            });
          } else {
            this.$notify({
              type: "warning",
              title: `重置失败`,
              message: response.data.data,
            });
          }
        })
        .then(() => {
          this.loadConfig();
        });
    },
    saveSettings() {
      this.checkChanged();
      if (Object.keys(this.changedSettings).length > 0) {
        this.submitChangedSettings();
        this.backupSettings = JSON.parse(JSON.stringify(this.model));
        this.changedSettings = {};
      } else {
        this.$notify({
          type: "warning",
          title: `设置失败`,
          message: "你没有更改任何设置哦",
        });
      }
    },
    submitChangedSettings() {
      let submitCache = {
        cfgs: [],
      };
      for (let key of Object.keys(this.changedSettings)) {
        submitCache.cfgs.push({
          name: key,
          content: this.changedSettings[key],
        });
      }
      console.log(JSON.stringify(submitCache));
      axios
        .post(CONFIG.backend + "/api/settings", submitCache)
        .then((response) => {
          if (response.data.code == 0) {
            this.$notify({
              type: "info",
              title: `设置成功`,
            });
          } else {
            this.$notify({
              type: "warning",
              title: `设置失败`,
              message: response.data.data,
            });
          }
          console.log(response);
        });
    },
  },
  watch: {},
  mounted: function() {
    this.loadConfig();
  },
};
</script>
<style></style>
