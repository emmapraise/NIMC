<template>
	<div class="">
		<header-vue />
		<b-row>
			<b-col></b-col>
			<b-col md="9">
				<b-card class="mx-auto mt-3" title="Admin Sign Up">
					<b-form @submit.prevent="onSubmit">
						<b-row
							v-for="(item, index) in admin_signup"
							:key="index"
							class="my-2"
						>
							<b-col sm="3">
								<label :for="item.label">{{ item.name }}</label>
							</b-col>
							<b-col sm="9">
								<div v-if="item.type === 'radio'">
									<b-form-radio-group
										:id="item.label"
										v-model="item.value"
										required
										:options="item.options"
									></b-form-radio-group>
								</div>
								<div v-else-if="item.type === 'select'">
									<b-form-select
										:id="item.label"
										v-model="item.value"
										required
										:options="item.options"
									></b-form-select>
								</div>
								<div v-else>
									<b-form-input
										:type="item.type"
										:placeholder="item.placeholder"
										v-model="item.value"
									></b-form-input>
								</div>
							</b-col>
						</b-row>
						<b-button variant="success" class="mt-3" type="submit"
							>Sign Up</b-button
						>
					</b-form>
				</b-card>
			</b-col>
			<b-col></b-col>
		</b-row>
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
					name: 'First Name',
					label: 'first_name',
					type: 'text',
					value: '',
					placeholder: 'Enter First Name',
					icon: 'person-fill',
				},
				{
					name: 'Middle Name',
					label: 'middle_name',
					type: 'text',
					value: '',
					placeholder: 'Enter Middle Name',
					icon: 'person-fill',
				},
				{
					name: 'Last Name',
					label: 'last_name',
					type: 'text',
					value: '',
					placeholder: 'Enter Last Name',
					icon: 'person-fill',
				},
				{
					name: 'Gender',
					label: 'gender',
					type: 'radio',
					value: null,
					placeholder: 'Enter Gender',
					options: [
						{ value: 'M', text: 'Male' },
						{ value: 'F', text: 'Female' },
					],
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
				{
					name: 'Government',
					label: 'type',
					type: 'select',
					value: null,
					placeholder: 'Choose a Government',
					options: [
						{
							value: null,
							text: 'Choose a Government Type',
						},
						{
							value: 'Local Government',
							text: 'Local Government',
						},
						{
							value: 'State Government',
							text: 'State Government',
						},
						{
							value: 'Federal Government',
							text: 'Federal Government',
						},
					],
					icon: 'person-fill',
				},
			],
		};
	},
	methods: {
		onSubmit() {
			const data = this.admin_signup.reduce(
				(acc, cur) => ({ ...acc, [cur.label]: cur.value }),
				{}
			);
			this.data = {};
			this.data['type'] = data.type;
			delete data.type;
			this.data['user'] = data;
			this.data.user.avatar = null;
			this.axios
				.post('api/admin/', this.data)
				.then(() => {
					this.$router.push({ name: 'login' });
				})
				.catch(() => {});
		},
	},
};
</script>
