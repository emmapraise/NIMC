<template>
	<div class="container">
		<b-row class="my-2" v-for="(item, index) in kinship_tab" :key="index">
			<b-col sm="3">
				<label :for="item.label"> {{ item.name }}</label>
			</b-col>
			<b-col sm="9">
				<div v-if="item.type === 'textarea'">
					<b-form-textarea
						:id="item.label"
						max-rows="6"
						rows="3"
						required
						v-model="item.value"
					>
					</b-form-textarea>
				</div>
				<div v-else>
					<b-form-input
						:id="item.label"
						:type="item.type"
						required
						v-model="item.value"
					></b-form-input>
				</div>
			</b-col>
		</b-row>
	</div>
</template>
<script>
export default {
	name: 'KinshipData',
	data() {
		return {
			kinship_tab: [
				{
					name: 'Next of Kin',
					label: 'next_of_kin',
					type: 'text',
					value: '',
				},
				{
					name: 'Next of Kin Email',
					label: 'next_of_kin_email',
					type: 'email',
					value: '',
				},
				{
					name: 'Next of Kin Phone Number',
					label: 'next_of_kin_phone',
					type: 'tel',
					value: '',
				},
				{
					name: 'Next of Kin Address',
					label: 'next_of_kin_address',
					type: 'textarea',
					value: '',
				},
			],
		};
	},
};
</script>
