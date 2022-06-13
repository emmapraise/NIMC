<template>
	<div class="">
		<header-vue />
		<b-row class="mt-2">
			<b-col md="2">
				<sidebar-vue />
			</b-col>
			<b-col md="10">
				<b-card title="Enrol A User" class="">
					<b-form
						@submit.prevent="onSubmit"
						validated="true"
						class="was-validated"
					>
						<user-profile />
						<!-- <div class="mt-5 float-right" align-h="end">
					<b-button size="lg" variant="success">Submit</b-button>
				</div> -->
					</b-form>
				</b-card>
			</b-col>
		</b-row>
	</div>
</template>
<script>
import HeaderVue from '../../components/header/Header.vue';
import SidebarVue from '../../components/sidebar/Sidebar.vue';
import UserProfile from '../../components/profile/UserProfile.vue';
export default {
	name: 'RegisterView',
	components: {
		UserProfile,
		HeaderVue,
		SidebarVue,
	},
	data() {
		return {};
	},
	mounted() {},
	methods: {
		onsubmit() {
			console.log('object');
		},
	},
};
</script>
