<template>
	<div class="">
		<header-vue />
		<b-card class="mx-auto w-25 mt-3" title="Admin Sign Up">
			<b-form @submit.prevent="onSubmit">
				<div v-for="(item, index) in admin_signup" :key="index">
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
				<b-button variant="success" block class="mt-3" type="submit"
					>Sign Up</b-button
				>
			</b-form>
		</b-card>
	</div>
</template>
<script>
import HeaderVue from '../../components/header/Header.vue';
export default {
	name: 'AdminSignUp',
	components: {
		HeaderVue,
	},
	data() {
		return {
			admin_signup: [
				{
					name: 'Username',
					label: 'username',
					type: 'text',
					value: '',
					placeholder: 'Enter Username',
					icon: 'person-fill',
				},
				{
					name: 'Email Address',
					label: 'email',
					type: 'email',
					value: '',
					placeholder: 'Enter Email Address',
					icon: 'envelope-fill',
				},
				{
					name: 'Phone Number',
					label: 'phone',
					type: 'tell',
					value: '',
					placeholder: 'Enter Phone Number',
					icon: 'telephone-fill',
				},
				{
					name: 'Password',
					label: 'password',
					type: 'password',
					placeholder: 'Enter Password',
					icon: 'lock-fill',
				},
			],
		};
	},
	methods: {
		onSubmit() {
			this.data = this.admin_signup.reduce(
				(acc, cur) => ({ ...acc, [cur.label]: cur.value }),
				{}
			);
			this.axios
				.post('api/admin/', this.data)
				.then((result) => {
					console.log('success', result);
				})
				.catch((err) => {
					console.log('error', err);
				});
			console.log(this.data);
		},
	},
};
</script>
