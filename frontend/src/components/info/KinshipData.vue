<template>
	<div class="">
		<b-row>
			<b-col
				class="my-1"
				v-for="(item, index) in kinship_tab"
				:key="index"
				md="6"
			>
				<b-row>
					<b-col md="3">
						<label :for="item.label"> {{ item.name }}</label>
					</b-col>
					<b-col md="9">
						<div v-if="item.type === 'textarea'">
							<b-form-textarea
								:id="item.label"
								max-rows="6"
								rows="3"
								@input="emitValue"
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
								@input="emitValue"
								v-model="item.value"
							></b-form-input>
						</div> </b-col
				></b-row>
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
	methods: {
		emitValue() {
			const data = this.kinship_tab.reduce(
				(acc, cur) => ({ ...acc, [cur.label]: cur.value }),
				{}
			);
			this.$emit('kinshipData', data);
		},
	},
};
</script>
