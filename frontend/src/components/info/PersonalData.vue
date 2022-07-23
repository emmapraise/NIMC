<template>
	<div class="">
		<b-row>
			<b-col
				md="6"
				v-for="(item, index) in personal_data_tab"
				:key="index"
				class="my-1"
			>
				<b-row>
					<b-col md="4">
						<label :for="item.label">{{ item.name }}</label>
					</b-col>
					<b-col md="8">
						<template v-if="edit">
							<div v-if="item.label === 'marital_status'">
								<b-form-select
									:id="item.label"
									v-model="item.value"
									required
									@change="emitValue"
									:options="item.options"
								></b-form-select>
							</div>
							<div v-else-if="item.type === 'textarea'">
								<b-form-textarea
									:id="item.label"
									max-rows="6"
									@input="emitValue"
									required
									rows="3"
									v-model="item.value"
								>
								</b-form-textarea>
							</div>
							<div v-else>
								<b-form-input
									:id="item.label"
									required
									:type="item.type"
									v-model="item.value"
									@input="emitValue"
								></b-form-input>
							</div>
						</template>
						<template v-else> {{ item.value }}</template>
					</b-col></b-row
				>
			</b-col>
		</b-row>
	</div>
</template>
<script>
export default {
	name: 'PersonalDataComponents',
	props: {
		getData: Object,
		isAdmin: Boolean,
		edit: Boolean,
	},
	data() {
		return {
			personal_data_tab: [
				{
					name: 'Date of Birth',
					label: 'date_of_birth',
					type: 'date',
					value: '',
				},
				{
					name: 'State of Origin',
					label: 'state_of_origin',
					type: 'text',
					value: '',
				},
				{
					name: 'Occupation',
					label: 'occupation',
					type: 'text',
					value: '',
				},
				{
					name: 'Marital Status',
					label: 'marital_status',
					type: 'select',
					value: null,
					options: [
						{
							value: null,
							text: 'Please select an Option',
						},
						{
							value: 'Single',
							text: 'Single',
						},
						{
							value: 'Married',
							text: 'Married',
						},
						{
							value: 'Divorced',
							text: 'Divorced',
						},
					],
				},

				{
					name: 'Home Address',
					label: 'address',
					type: 'textarea',
					value: '',
				},
			],
		};
	},
	mounted() {
		if (!this.isAdmin) {
			this.loadData();
		}
	},
	methods: {
		emitValue() {
			const data = this.personal_data_tab.reduce(
				(acc, cur) => ({ ...acc, [cur.label]: cur.value }),
				{}
			);
			this.$emit('personalData', data);
		},
		loadData() {
			this.personal_data_tab.map((item) => {
				const asArray = Object.entries(this.getData);
				const filtered = asArray.filter(([key]) => key === item['label']);
				const justStrings = Object.fromEntries(filtered);
				return (item['value'] = justStrings[item['label']]);
			});
		},
	},
};
</script>
