<template>
	<div class="">
		<header-vue />
		<b-row>
			<b-col md="3"> </b-col>
			<b-col md="6">
				<b-card class="mx-auto mt-3" title="Check NIN">
					<b-form @submit.prevent="onSubmit">
						<div v-for="(item, index) in checkin_data" :key="index">
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
							>Check In</b-button
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
	name: 'PartnerCheckIn',
	components: {
		HeaderVue,
	},
	data() {
		return {
			data: {},
			isError: false,
			errorMessage: '',
			checkin_data: [
				{
					name: 'NIN',
					label: 'nin',
					type: 'text',
					icon: 'person-fill',
					value: '',
					placeholder: 'Enter NIN',
				},
				{
					name: 'Access Code',
					label: 'access_code',
					type: 'password',
					icon: 'upc-scan',
					value: '',
					placeholder: 'Enter Access Code',
				},
			],
		};
	},
	methods: {
		async onSubmit() {
			this.data = this.checkin_data.reduce(
				(acc, cur) => ({ ...acc, [cur.label]: cur.value }),
				{}
			);
			await this.axios
				.post(`api/patner-access/`, this.data)
				.then(({ data }) => {
					this.isError = false;
					localStorage.setItem('nininfo', JSON.stringify(data));
					this.$router.push({ name: 'patner_user_profile' });
				})
				.catch((err) => {
					this.isError = true;
					this.errorMessage = err.response.data.detail;
					console.error(err);
				});
		},
	},
};
</script>
