<template>
	<div class="">
		<header-vue />
		<b-card class="mx-auto w-25 mt-3" title="User Login">
			<b-form @submit.prevent="onSubmit">
				<div v-for="(item, index) in login_data" :key="index">
					<b-input-group class="mb-2 mt-2">
						<b-input-group-prepend is-text>
							<b-icon :icon="item.icon"></b-icon>
						</b-input-group-prepend>
						<b-form-input
							:type="item.type"
							:placeholder="item.placeholder"
							v-model="item.value"
						></b-form-input>
					</b-input-group>
				</div>

				<b-button variant="success" block class="mt-3" type="onSubmit"
					>Login</b-button
				>
			</b-form>
			<div v-show="isError" class="mt-2">
				<b-alert show variant="danger" dismissible>{{ errorMessage }} </b-alert>
			</div>
		</b-card>
	</div>
</template>
<script>
import HeaderVue from '../../components/header/Header.vue';
export default {
	name: 'LoginView',
	components: {
		HeaderVue,
	},
	data() {
		return {
			login_data: [
				{
					name: 'NIN',
					label: 'username',
					type: 'text',
					icon: 'person-fill',
					value: '',
					placeholder: 'Enter NIN',
				},
				{
					name: 'Password',
					label: 'password',
					type: 'password',
					icon: 'lock-fill',
					value: '',
					placeholder: 'Enter Password',
				},
			],
			isError: false,
			errorMessage: '',
		};
	},
	methods: {
		onSubmit() {
			this.data = this.login_data.reduce(
				(acc, cur) => ({ ...acc, [cur.label]: cur.value }),
				{}
			);
			this.axios
				.post('api/login/', this.data)
				.then((result) => {
					const token = result.data.refresh;
					this.$store.commit('setToken', token);
					this.axios.defaults.headers.common['Authorization'] =
						'Token ' + token;
					localStorage.setItem('token', token);
					this.$router.push({ name: 'enrolment' });
				})
				.catch((err) => {
					this.isError = true;
					this.errorMessage = err.response.data.detail;
				});
		},
	},
};
</script>
