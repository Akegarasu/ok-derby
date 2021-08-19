<template>
  <nav
    class="navbar navbar-vertical fixed-left navbar-expand-md navbar-light bg-white"
    id="sidenav-main"
  >
    <div class="container-fluid">
      <!--Toggler-->
      <navbar-toggle-button @click.native="showSidebar">
        <span class="navbar-toggler-icon"></span>
      </navbar-toggle-button>
      <router-link class="navbar-brand" to="/">
        <img :src="logo" class="navbar-brand-img" alt="..." />
      </router-link>

      <slot name="mobile-right">
        <ul class="nav align-items-center d-md-none">
          <base-dropdown class="nav-item" position="right">
            <a
              slot="title"
              class="nav-link nav-link-icon"
              href="#"
              role="button"
              data-toggle="dropdown"
              aria-haspopup="true"
              aria-expanded="false"
            >
              <i class="ni ni-bell-55"></i>
            </a>

            <a class="dropdown-item" href="#">Action</a>
            <a class="dropdown-item" href="#">Another action</a>
            <div class="dropdown-divider"></div>
            <a class="dropdown-item" href="#">Something else here</a>
          </base-dropdown>
          <base-dropdown class="nav-item" position="right">
            <a slot="title" class="nav-link" href="#" role="button">
              <div class="media align-items-center">
                <span class="avatar avatar-sm rounded-circle">
                  <img
                    alt="Image placeholder"
                    src="img/theme/specialweek.png"
                  />
                </span>
              </div>
            </a>

            <div class=" dropdown-header noti-title">
              <h6 class="text-overflow m-0">欢迎!</h6>
            </div>
            <router-link to="/settings" class="dropdown-item">
              <i class="ni ni-settings-gear-65"></i>
              <span>设置</span>
            </router-link>
            <div class="dropdown-divider"></div>
            <a href="#!" class="dropdown-item">
              <i class="ni ni-user-run"></i>
              <span>RUA！</span>
            </a>
          </base-dropdown>
        </ul>
      </slot>
      <slot></slot>
      <div
        v-show="$sidebar.showSidebar"
        class="navbar-collapse collapse show"
        id="sidenav-collapse-main"
      >
        <div class="navbar-collapse-header d-md-none">
          <div class="row">
            <div class="col-6 collapse-brand">
              <router-link to="/">
                <img :src="logo" />
              </router-link>
            </div>
            <div class="col-6 collapse-close">
              <navbar-toggle-button
                @click.native="closeSidebar"
              ></navbar-toggle-button>
            </div>
          </div>
        </div>

        <ul class="navbar-nav">
          <slot name="links"> </slot>
        </ul>
        <!--Divider-->
        <hr class="my-3" />
        <!--Heading-->
        <h6 class="navbar-heading text-muted">文档</h6>
        <!--Navigation-->
        <ul class="navbar-nav mb-md-3">
          <li class="nav-item">
            <a
              class="nav-link"
              href="https://github.com/Akegarasu/ok-derby"
            >
              <i class="ni ni-spaceship"></i> 使用教程
            </a>
          </li>
          <li class="nav-item">
            <a class="nav-link" href="https://afdian.net/@akibanzu">
              <i class="ni ni-palette"></i> 支持作者
            </a>
          </li>
          <li class="nav-item">
            <a class="nav-link" href="https://anzu.link">
              <i class="ni ni-ui-04"></i> 作者主页
            </a>
          </li>
        </ul>
      </div>
    </div>
  </nav>
</template>
<script>
import NavbarToggleButton from "@/components/NavbarToggleButton";

export default {
  name: "sidebar",
  components: {
    NavbarToggleButton,
  },
  props: {
    logo: {
      type: String,
      default: "img/brand/green.png",
      description: "Sidebar app logo",
    },
    autoClose: {
      type: Boolean,
      default: true,
      description:
        "Whether sidebar should autoclose on mobile when clicking an item",
    },
  },
  provide() {
    return {
      autoClose: this.autoClose,
    };
  },
  methods: {
    closeSidebar() {
      this.$sidebar.displaySidebar(false);
    },
    showSidebar() {
      this.$sidebar.displaySidebar(true);
    },
  },
  beforeDestroy() {
    if (this.$sidebar.showSidebar) {
      this.$sidebar.showSidebar = false;
    }
  },
};
</script>
