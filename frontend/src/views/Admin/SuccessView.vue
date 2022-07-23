<template>
	<div>
		<header-vue :logout="true" />
		<b-row class="mt-2">
			<b-col md="2">
				<sidebar-vue />
			</b-col>
			<b-col md="10">
				<div class="">
					<h1>Account Created Successfully</h1>
					<b-row>
						<b-col md="6">
							<p>
								Below is the User information <br />
								Login using the email and password below. Password can be
								changed once login
							</p>
							<h4>
								NIN: <small>{{ data.nin }}</small>
							</h4>
							<h4>
								Full name:
								<small
									>{{ data.first_name }} {{ data.middle_name }}
									{{ data.last_name }}</small
								>
							</h4>
							<h4>
								Phone: <small>{{ data.phone }}</small>
							</h4>
							<h4>
								Email: <small>{{ data.email }}</small>
							</h4>
							<h4>
								Password:
								<small>{{ password }}</small>
							</h4>
							<h4>
								Passcode: <small>{{ data.access_code }}</small>
							</h4>
						</b-col>
						<b-col md="6">
							<p>Scan or download the Barcode to get the login details</p>
							<div class="mx-auto">
								<b-img
									src="https://picsum.photos/300/150/?image=41"
									fluid
									alt="Fluid image"
								></b-img>
							</div>
						</b-col>
					</b-row>
				</div>
			</b-col>
		</b-row>
	</div>
</template>
<script>
import HeaderVue from '@/components/header/Header.vue';
import SidebarVue from '@/components/sidebar/Sidebar.vue';
export default {
	name: 'SuccessView',
	components: {
		HeaderVue,
		SidebarVue,
	},
	props: ['user'],
	data() {
		return {
			password: '',
			data: {},
		};
	},
	mounted() {
		this.data = this.$route.params.user;
		this.password = process.env.VUE_APP_DEFAULT_PASSWORD;
	},
};
</script>
