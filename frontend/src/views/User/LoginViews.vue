<template>
	<div class="">
		<header-vue />
		<b-row>
			<b-col md="3"></b-col>
			<b-col md="6">
				<b-card class="mx-auto mt-3" title="User Login">
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
						<b-alert show variant="danger" dismissible
							>{{ errorMessage }}
						</b-alert>
					</div>
				</b-card>
			</b-col>
			<b-col md="3"></b-col>
		</b-row>
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
					const token = result.data.data.tokens.access;
					const user = JSON.stringify(result.data.data.user);
					this.$store.commit('setToken', token, user);
					this.axios.defaults.headers.common['Authorization'] =
						'Bearer ' + token;
					localStorage.setItem('token', token);
					localStorage.setItem('user', user);
					user.is_admin
						? this.$router.push({ name: 'enrolment' })
						: this.$router.push({ name: 'make-request' });
				})
				.catch((err) => {
					this.isError = true;
					this.errorMessage = err.response.data.detail;
				});
		},
	},
};
</script>
